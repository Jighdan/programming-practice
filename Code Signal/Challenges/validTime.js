/*
Check if the given string is a correct time representation of the 24-hour clock.
*/

const validTime = time => {
    let re = /^[0-1]/
	if (re.test(time)) {
		re = /^[0-1][0-9]:[0-5][0-9]/;
		return re.test(time);
	} else {
        if (/[0][0]$/.test(time)) {
            return false
        }
        
		re = /^[0-2][0-4]:[0-5][0-9]/;
		return re.test(time);
	}
};
