#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let n_occurs = 0;
  for (let i = 0; i < list.length; i++) {
    if (searchElement === list[i]) {
      n_occurs++;
    }
  }
  return n_occurs;
};
