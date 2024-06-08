var close = document.getElementsByClassName("close");
var i;

const button = document.getElementById('new');
button.addEventListener('click', () => {
  window.location.href = "{{ url_for('routes.new_record') }}"; 
});
for (i = 0; i < close.length; i++) {
  close[i].onclick = function(){
    var div = this.parentElement;
    div.style.opacity = "0";
    setTimeout(function(){ div.style.display = "none"; }, 600);
  }
}