function bs(arr, left, right, needle) {
  // debugger;
  // base case
  if (left > right) return -1;

  var mid = Math.floor((right+left)/2);
  if(arr[mid] == needle) return mid;
  if(needle < arr[mid]) {
    return bs(arr, left, mid-1, needle);
  }
  else {
    return bs(arr, mid+1, right, needle);
  }
}

var primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

var res = bs(primes, 0, primes.length - 1, 4);
console.log(res);