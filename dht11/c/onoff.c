/*  Python module for DHT temperature/humidity sensors
 *
 *  Modified by Qingping Hou from DHT reader example, original header:
 *
 *  How to access GPIO registers from C-code on the Raspberry-Pi
 *  Example program
 *  15-January-2012
 *  Dom and Gert
 */


/* for usleep */
#define _BSD_SOURCE

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <dirent.h>
#include <fcntl.h>
#include <assert.h>
#include <unistd.h>
#include <sys/mman.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <sys/time.h>
// #include <bcm2835.h>
#include <mraa.h>
#include <unistd.h>

// #include <Python.h>

#define MAXTIMINGS 100

//#define DEBUG

#define DHT11 11
#define DHT22 22
#define AM2302 22

int main(int argc, char* argv[]) {
    int i, pin;

    if (argc != 2) {
        printf("Input GPIO number...");
        exit(1);
    }

    pin = atoi(argv[1]);

    printf("GPIO >>> %d\n", pin);

    mraa_gpio_context gpio;

    gpio = mraa_gpio_init(pin);

    mraa_gpio_dir(gpio, MRAA_GPIO_OUT);

    while (1) {
        mraa_gpio_write(gpio, 0);
        usleep(60000);

        mraa_gpio_write(gpio, 1);
        usleep(60000);
    }

    mraa_gpio_close(gpio);

    return 0;
}