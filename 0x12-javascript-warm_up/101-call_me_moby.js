#!/usr/bin/node
exports.callMeMoby = function func (x, theFunction) {
	theFunction();
	if (x && --x) {
    	 func(x, theFunction);
	}
};
