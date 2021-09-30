let rFib = (n) => {
  if (n === 0) {
    return 0;
  } else if (n === 1 || n === 2) {
    return 1
  } else {
    return rFib(n - 1) + rFib(n - 2)
  }
}

console.log(
  rFib(4)
);