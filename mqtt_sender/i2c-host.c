#include <stdio.h>
#include <unistd.h>
#include <errno.h>
#include <stdlib.h>
#include <stdint.h>
#include <linux/i2c-dev.h>
#include <fcntl.h>

typedef struct {
	int16_t		ac1;
	int16_t		ac2;
	int16_t		ac3;
	uint16_t	ac4;
	uint16_t	ac5;
	uint16_t	ac6;
	int16_t		b1;
	int16_t		b2;
	int16_t		mb;
	int16_t		mc;
	int16_t		md;
} bmp085_calib_data;

#define ACC_ADDRESS		(0x53)
#define PRESS_ADDRESS		(0x77)

#define DATA_REG_START 		(0x32)
#define POWER_CTRL_REG		(0X2D)


void write_two(int file, char target, char value) {
	char buf[2];
	buf[0] = target;
	buf[1] = value;
	if(write(file, buf, 2) != 2) {
		printf("error: failed to write\n");
		exit(1);
	}
}

void write_single(int file, char value) {
	char buf[2];
	buf[0] = value;
	if(write(file, buf, 1) != 1) {
		printf("error: failed to write 1\n");
		exit(1);
	}
}

char readRegister(int file, char reg) {
	char buf[2];
	write_single(file, reg);

	if(read(file, buf, 1) != 1) {
		printf("error: failed to read\n");
		exit(1);
	}
	return buf[0];
}

int16_t readX(int file) {
	int16_t result = 0;
	result = readRegister(file, DATA_REG_START) | (readRegister(file, DATA_REG_START + 1) << 8);
	return result;	
}

int16_t readY(int file) {
	int16_t result = 0;
	result = readRegister(file, DATA_REG_START + 2) | (readRegister(file, DATA_REG_START + 3) << 8);
	return result;	
}

int16_t readZ(int file) {
	int16_t result = 0;
	result = readRegister(file, DATA_REG_START + 4) | (readRegister(file, DATA_REG_START + 5) << 8);
	return result;	
}

int32_t computeB5(int32_t ut, bmp085_calib_data * calibration) {
	int32_t X1 = (ut - (int32_t)calibration->ac6) * ((int32_t)calibration->ac5) >> 15;
	int32_t X2 = ((int32_t)calibration->mc << 11) / (X1+(int32_t)calibration->md);
	return X1 + X2;
}

float readTemp(int file, bmp085_calib_data * calibration) {
	write_two(file, 0xF4, 0x2E);
	usleep(20);
	int32_t result = (readRegister(file, 0xF6) << 8) | readRegister(file, 0xF6 + 1); 
	int32_t b5 = computeB5(result, calibration);
	float temp = ((b5  + 8) >> 4);
	return temp / 10.0;
}

int connect_accel(const char * devName) {
	int file = open(devName, O_RDWR);
	if(file == -1) {
		printf("error: could not open %s\n", devName); 
		exit(1);
	}

	if(ioctl(file, I2C_SLAVE, ACC_ADDRESS) < 0) {
		printf("error: failed to acquire bus address and or talk to slave\n");
		exit(1);
	}
	return file;
}

void readCalabrationStuff(int file, bmp085_calib_data * cal) {
	cal->ac1 = (readRegister(file, 0xAA) << 8) | readRegister(file, 0xAA +1);
	cal->ac2 = (readRegister(file, 0xAC) << 8) | readRegister(file, 0xAC + 1);
	cal->ac3 = (readRegister(file, 0xAE) << 8) | readRegister(file, 0xAE + 1);
	cal->ac4 = (readRegister(file, 0xB0) << 8) | readRegister(file, 0xB0 + 1);
	cal->ac5 = (readRegister(file, 0xB2) << 8) | readRegister(file, 0xB2 + 1);
	cal->ac6 = (readRegister(file, 0xB4) << 8) | readRegister(file, 0xB4 + 1);

	cal->b1 = (readRegister(file, 0xB6) << 8) | readRegister(file, 0xB6 + 1);
	cal->b2 = (readRegister(file, 0xB8) << 8) | readRegister(file, 0xB8 + 1);

	cal->mb = (readRegister(file, 0xBA) << 8) | readRegister(file, 0xBA + 1);
	cal->mc = (readRegister(file, 0xBC) << 8) | readRegister(file, 0xBC + 1);
	cal->md = (readRegister(file, 0xBE) << 8) | readRegister(file, 0xBE + 1);
}

void enable_pressure(int file, bmp085_calib_data * calibration) {
	if(ioctl(file, I2C_SLAVE, PRESS_ADDRESS) < 0) {
		printf("error: failed to acquire bus address or talk to pressure sensor\n");
		exit(1);
	}

	readCalabrationStuff(file, calibration);
}

void enable_accel(int file) {

	if(ioctl(file, I2C_SLAVE, ACC_ADDRESS) < 0) {
		printf("error: failed to acquire bus address and or talk to slave\n");
		exit(1);
	}


	write_two(file, POWER_CTRL_REG, 0x08);
	
}

int main(int argc, char** argv) {

	const char * devName = "/dev/i2c-1";

	bmp085_calib_data calibration;
	
	int file = connect_accel(devName);

	enable_accel(file);

	printf("x: %d y: %d z: %d\n", readX(file), readY(file), readZ(file));

	enable_pressure(file, &calibration);

	printf("temp: %f\n", readTemp(file, &calibration));

	return 0;
}
