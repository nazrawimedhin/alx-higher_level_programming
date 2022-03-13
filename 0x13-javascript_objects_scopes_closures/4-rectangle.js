#!/usr/bin/node
class Rectangle{
    constructor(w, h) {
        if ((w > 0) && (h > 0)){
            this.width = w;
            this.height = h;
        }
    }
        print(){
            let rect = '';
            for (let i = 0; i < h; i++) {
                for (let j = 0; j < w; j++) {
                    rect += 'X';
                }
                rect += '\n';
            }
            console.log(rect);
        }

        rotate(){
            let rect = '';
            for (let i = 0; i < w; i++) {
                for (let j = 0; j < h; j++) {
                    rect += 'X';
                }
                rect += '\n';
            }
            console.log(rect);
        }
        
        print(){
            let rect = '';
            for (let i = 0; i < 2*h; i++) {
                for (let j = 0; j < 2*w; j++) {
                    rect += 'X';
                }
                rect += '\n';
            }
            console.log(rect);
        }
};

module.exports = Rectangle;