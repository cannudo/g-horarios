function doAjax(botao) {
  idDoProfessor = botao.value;
  csrf = document.getElementById("csrf").innerText;

  var request = new XMLHttpRequest();
  request.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      document.getElementById("receberDados").innerHTML = this.responseText;
    }
  };
}
