angular.module('CadastroApp', [])
  .controller('CadastroController', function () {
    var vm = this;
    vm.usuario = {
      username: '',
      name: '',
      email: '',
      password: ''
    };

    vm.submitForm = function () {
      axios.post('http://localhost:8000/', vm.usuario)
        .then(function (response) {
          console.log('Dados enviados com sucesso para o backend:', response.data);
          console.log('response.status = ', response.status)

          vm.usuario = { // clean form fields
            username: '',
            name: '',
            email: '',
            password: ''
          };
        })
        .catch(function (error) {
          console.error('error-type:', error.response.data);
          console.error('error-status = ', error.response.status);
        });
    };
  });


function reloadDelay(time) {
  setTimeout(function () {
    location.reload();
  }, time * 1000);
}
