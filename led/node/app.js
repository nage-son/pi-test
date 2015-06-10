var Gpio = require('onoff').Gpio,
    led1 = new Gpio(25, 'out'),
    led2 = new Gpio(24, 'out'),
    led3 = new Gpio(23, 'out');

var sleep = require('sleep');

process.on('exit', function() {
    console.log('exit program!');
    led1.write(0, function(err){});
    led2.write(0, function(err){});
    led3.write(0, function(err){});
});

(function blink() {
    led1.read(function(err, value) {
        if (err) {
            throw err;
        }

        if (value) {
            console.log('on');
        } else {
            console.log('off');
        }

        led1.write(value ^ 1, function(err) {
            if (err) {
                throw err;
            }
        });
    });

    setTimeout(function() {
        blink();
    }, 200);
    
    while (true) {
        led1.write(1, function(err) {
            if (err) {
                throw err;
            }
        });

        led2.write(0, function(err) {
            if (err) {
                throw err;
            }
        });

        led3.write(0, function(err) {
            if (err) {
                throw err;
            }
        });

        sleep.usleep(100000);

        led1.write(0, function(err) {
            if (err) {
                throw err;
            }
        });

        led2.write(1, function(err) {
            if (err) {
                throw err;
            }
        });

        led3.write(0, function(err) {
            if (err) {
                throw err;
            }
        });

        sleep.usleep(100000);

        led1.write(0, function(err) {
            if (err) {
                throw err;
            }
        });

        led2.write(0, function(err) {
            if (err) {
                throw err;
            }
        });

        led3.write(1, function(err) {
            if (err) {
                throw err;
            }
        });

        sleep.usleep(100000);
    }
}());