var procurar = $("#procurar")



procurar.addEventListener("input", function() {
    console.log(this.value);
    var pacientes = document.querySelectorAll(".paciente");

    if(this.value.length > 0) {
        for ( var i = 0; i < pacientes.length ; i++) {
            var paciente = pacientes[i]
            var nome = paciente.querySelector(".name-paciente");
            var npaciente = nome.textContent();
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
})