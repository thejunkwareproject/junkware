// Junk object

var Junk = function() {

    var self = this;

    /*
      MODEL

      self.
      self.createdAt      : Date

    */

}

function isValidDate(d) {
  if ( Object.prototype.toString.call(d) !== "[object Date]" )
    return false;
  return !isNaN(d.getTime());
}

function isNumber(n) {
  return !isNaN(parseFloat(n)) && isFinite(n);
}
