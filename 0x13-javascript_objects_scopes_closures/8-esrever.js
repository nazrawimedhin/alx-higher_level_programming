exports.esrever = function (list){
    let len = list.length - 1;
    let i = 0;
    while (i < len) {
        const aux = list[len];
        list[len] = list[i];
        list[i] = aux;
        i++;
        len--;
    }
};