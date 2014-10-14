define(function() {
  var stats = new Stats();
  stats.domElement.style.position = 'fixed';
  stats.domElement.style.top = '50px';
  stats.domElement.style.left = '20px';
  document.getElementById("container").appendChild(stats.domElement);
  return stats;
});
