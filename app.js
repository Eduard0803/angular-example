angular.module('CadastroApp', [])
  .controller('CadastroController', function () {
    var vm = this;
    vm.usuario = {
      name: '',
      email: '',
      password: ''
    };

    vm.submitForm = function () {
      axios.post('http://localhost:8000/', vm.usuario)
        .then(function (response) {
          console.log('Dados enviados com sucesso para o backend:', response.data);
          // Limpar os campos do formulário após o envio bem-sucedido
          vm.usuario = {
            name: '',
            email: '',
            password: ''
          };
        })
        .catch(function (error) {
          console.error('Erro ao enviar dados para o backend:', error);
        });
    };
  });


function reloadDelay(time) {
  setTimeout(function () {
    location.reload();
  }, time * 1000);
}
