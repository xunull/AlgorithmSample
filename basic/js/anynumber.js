/**
 * 任意进制的运算
 */

// 引入了readline 使用完后就必须调用close 方法,否则程序不会终止
var readline = require('readline');

var rl = readline.createInterface({
    input: process.stdin,
    // 如果不设置output ,当使用readline 的question 方法的时候不会有输出
    output: process.stdout
});

// rl.setPrompt('>>');
// rl.prompt();

// rl.on('line', (cmd) => {
//   console.log(`You just typed: ${cmd}`);
// });

rl.question('请输入十进制数字,将其转化为特殊进制 ', (answer) => {
    // TODO: Log the answer in a database
    console.log('Thank you for your valuable feedback:', answer);
    console.log('result is ', tenToAny(answer, 4));
});

// rl.question('请输入任意进制的数,将其转化为10进制', (answer) => {
//     console.log('result is ', anyToTen(answer, 3));
//     rl.close();
// });

function tenToAny(number, any) {
    var result_arr = [];
    var remainder;
    var quotient;
    if (number < any) {
        return number;
    }
    do {
        remainder = number % any;
        result_arr.unshift(remainder);
        number = Math.floor(number / any);
    } while (number >= any);
    result_arr.unshift(number);

    return +result_arr.join('');
}

function anyToTen(number, any) {
    number = '' + number;
    number_arr = number.split('');
    var length = number_arr.length;
    // 这个如果不设置成0 result 会是NaN
    var result = 0;
    for (var i = 0; i < length; i++) {
        result += (+number_arr[i]) * Math.pow(any, length - i - 1);
    }
    return result;
}
