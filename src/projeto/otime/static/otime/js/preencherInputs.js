function doAjax(botao) {
  idDoProfessor = botao.value;
  csrf = document.getElementById("csrf").innerText;

  var request = new XMLHttpRequest();
  request.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      document.getElementById("receberDados").innerHTML = this.responseText;
    }
  };

  request.open("POST", "professores", true);
  request.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
  request.send("idDoProfessor=" + idDoProfessor + "&csrfmiddlewaretoken=" + csrf + "&ajax=1");
}
