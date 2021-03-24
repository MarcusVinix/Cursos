var botaoAdicionar = document.querySelector("#adicionar-paciente");
  
 botaoAdicionar.addEventListener("click", function(event){
    event.preventDefault(); 
    
    var form = document.querySelector("#form-adiciona");
    var paciente =  obtemPacienteDoFormulario(form);
    var erros = validaPaciente(paciente);

    if(erros.length > 0){
        var mensagemErros = document.querySelector("#mensagens-erros");
        exibeMensagemErro(erros);
        return;
    }
     
    adcionaPacienteNaTabela(paciente);
   
    form.reset();
    
    var mensagensErro = document.querySelector("#mensagens-erros");
    mensagensErro.innerHTML = "";
    
    
 });

 function adcionaPacienteNaTabela(paciente){
    
    var pacienteTr = montaTr(paciente);
    var tabela = document.querySelector("#tabela-pacientes");
    tabela.appendChild(pacienteTr);

}

 function obtemPacienteDoFormulario(form) {

    var paciente = {
        nome: form.nome.value,
        peso: form.peso.value,
        altura: form.altura.value,
        gordura: form.gordura.value,
        imc: calculaImc(form.peso.value, form.altura.value)
    }
    return paciente;
}

function montaTr(paciente){
    var pacienteTr = document.createElement("tr");
    pacienteTr.classList.add("paciente");

    pacienteTr.appendChild(montaTd(paciente.nome,"info-nome"));
    pacienteTr.appendChild(montaTd(paciente.peso,"info-peso"));
    pacienteTr.appendChild(montaTd(paciente.altura,"info-altura"));
    pacienteTr.appendChild(montaTd(paciente.gordura,"info-gordura"));
    pacienteTr.appendChild(montaTd(paciente.imc,"info-imc"));

    return pacienteTr;

}

function montaTd(dado,classe){
    var td = document.createElement("td");
    td.textContent = dado;
    td.classList.add(classe);

    return td;

}

function exibeMensagemErro(erros){
    var ul = document.querySelector("ul");
    ul.innerHTML = "";
    erros.forEach(function(erro){
        var li = document.createElement("li");
        li.textContent = erro;
        ul.appendChild(li);
    });

}

function validaPaciente(paciente){
    
    var erros = [];
    
    if(!validaPeso(paciente.peso)){
        erros.push("Peso Inválido!");
    }

    if(!validaAltura(paciente.altura)){
        erros.push("Altura Inválida!");
    }

    if(paciente.nome.length == 0){
        erros.push("O nome não pode ser em branco!");
    }
    
    if(paciente.peso.length == 0){
        erros.push("O peso não pode ser em branco!");
    }

    if(paciente.altura.length == 0){
        erros.push("A altura não pode ser em branco!");
    }
    if(paciente.gordura.length == 0){
        erros.push("A gordura não pode ser em branco!");
    }

    return erros;
}
