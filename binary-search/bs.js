var primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

function bs(arr, needle) {
	debugger;
	let arrSize = arr.length;
	let left = 0, right = arrSize - 1;
		
	while ( left <= right) {
		var middle = Math.floor((right + left)/2);
    
    // Found the guy \o/ 
		if (arr[middle] == needle) return middle;
    
    if (arr[middle] < needle) {
			left = middle + 1;
    }
		else {
			right = middle - 1;
    }	
	} 
	return -1;
}


bs(primes, 17)
bs(primes, 97)