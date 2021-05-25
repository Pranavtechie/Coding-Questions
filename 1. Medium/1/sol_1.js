const ValidateCards = (hand, width) => {
  let arr = hand;
  let blocks = [];
  while (arr.length > 0) {
    blocks.push(arr.splice(0, width));
  }
  return blocks[blocks.length - 1].length === width ? true : false;
};

let returnValue = ValidateCards([1, 2, 3, 6, 2, 3, 4, 7, 8], 3); // Question Values
console.log(returnValue);
