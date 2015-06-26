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

void get_data(mraa_gpio_context gpio, int* readData);

int main(int argc, char* argv[]) {
    mraa_gpio_context gpio;

    if (argc != 2) {
        printf("gpio [pin]\n");
        exit(1);
    }

    int pin = atoi(argv[1]);

    gpio = mraa_gpio_init(pin);

    if (gpio == NULL) {
        return 1;
    }

    // mraa_gpio_period_ms(4); // communication process is about 4ms(Data sheet)
    // Send start signal

    int readData = 0;
    int count = 0;

    printf("pin number %d\n", mraa_gpio_get_pin(gpio));
    
    while (1) {
        get_data(gpio, &readData);

        count++;

        if (count == 50) {
            printf("aaaa\n");
            break;
        }

        usleep(1000000);
    }

    mraa_gpio_close(gpio);

    printf("GPIO closed.\n");


    return 0;
}

void get_data(mraa_gpio_context gpio, int* readData) {
    mraa_gpio_dir(gpio, MRAA_GPIO_OUT);
    mraa_gpio_write(gpio, 1);
    mraa_gpio_write(gpio, 0);

    usleep(18000);

    mraa_gpio_write(gpio, 1);

    usleep(30);

    mraa_gpio_dir(gpio, MRAA_GPIO_IN);

    *readData = mraa_gpio_read(gpio);

    usleep(80);

    printf("first readData >>> %d\n", *readData);

    *readData = mraa_gpio_read(gpio);

    usleep(80);

    printf("second readData >>> %d\n", *readData);

    int i;

    for (i = 0; i < 40; i++) {
        *readData = mraa_gpio_read(gpio);

        printf("[%d] >>> %d\n", i, *readData);
    }
}