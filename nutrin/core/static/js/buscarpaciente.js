var procurar = $('#procurar');
var pacientes = $('.paciente')
var nome_pacientes = $('.nome-paciente')

procurar[0].addEventListener("input", function(){
    if (procurar[0].value.length > 0){
        for(var i = 0; i<pacientes.length; i++){
            paciente = pacientes[i];
            nome = nome_pacientes[i].textContent;
            var expressao = new RegExp(procurar[0].value, "i");
            if(! expressao.test(nome)){
                paciente.classList.add("esconder");
                paciente.style.display = "none";
            }
        }
    }else{
        var escondidos = $(".esconder")
        for(var i = 0; i<escondidos.length; i++){
            escondidos[i].classList.remove("esconder")
            escondidos[i].style.display = "";
        }
    }
});



/*procurar[0].addEventListener("input", function() {
    var pacientes = $("#pacientes");
    if(this.value.length > 0) {
        for ( var i = 0; i < pacientes.length ; i++) {
            var paciente = pacientes[i];
            var nome = $(".name-paciente");
            var npaciente = nome.innerHTML();
            var expressao = new RegExp(this.value, 'i')

            if (! expressao.test(npaciente)) {
                paciente.classList.add("Visível");
            }else {
                paciente.classList.add("Invisível");
            }
        }
    }
    else{
        for ( var i = 0 ; i < pacientes.length ; i++) {
            var paciente = pacientes[i]
            paciente.classList.remove("Invisível");
        }
    }
})*/