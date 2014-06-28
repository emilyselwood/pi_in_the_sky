#include <stdio.h>
#include <unistd.h>
#include <errno.h>
#include <stdlib.h>
#include <linux/i2c-dev.h>
#include <fcntl.h>

#define MAG_ADDRESS		(0x53)
#define DATA_REG_START 		(0x32)
#define POWER_CTRL_REG		(0X2D)

char readRegister(int file, char reg) {
	char buf[2];
	buf[0] = reg;
	if(write(file, buf, 1) != 1) {
		printf("error: failed to write\n");
		exit(1);
	}

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


int connect(const char * devName) {
	int file = open(devName, O_RDWR);
	if(file == -1) {
		printf("error: could not open %s\n", devName); 
		exit(1);
	}

	if(ioctl(file, I2C_SLAVE, MAG_ADDRESS) < 0) {
		printf("error: failed to acquire bus address and or talk to slave\n");
		exit(1);
	}
	return file;
}

void enable(int file) {
	char buf[2];
	buf[0] = POWER_CTRL_REG;
	buf[1] = 0x08;
	if(write(file, buf, 2) != 2) {
		printf("error: failed to write\n");
		exit(1);
	}
}

int main(int argc, char** argv) {

	const char * devName = "/dev/i2c-1";
	
	int file = connect(devName);

	enable(file);

	printf("x: %d y: %d z: %d\n", readX(file), readY(file), readZ(file));

	return 0;
}