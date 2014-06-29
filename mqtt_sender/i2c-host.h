
#include <stdint.h>

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

int connect_accel(const char * devName);

int16_t readX(int file);
int16_t readY(int file);
int16_t readZ(int file);

float readTemprature(int file, bmp085_calib_data * calibration);

void enable_pressure(int file, bmp085_calib_data * calibration);
void enable_accel(int file);


