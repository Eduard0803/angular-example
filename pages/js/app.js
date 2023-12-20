angular.module('CadastroApp', [])
    .controller('CadastroController', function () {
        var vm = this;
        vm.user = {
            username: '',
            name: '',
            email: '',
            password: ''
        };

        vm.submitForm = function () {
            const userValues = Object.values(vm.user);
            const ghostFields = userValues.filter(userValues => !userValues);
            if(ghostFields.length) // if field is empty
                return;
            axios.post('http://localhost:8000/', vm.user)
                .then(function (response) {
                    console.log('response.data:', response.data);
                    console.log('response.status =', response.status);

                    vm.user = { // clean form fields
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

function getUsers() {
    axios.get('http://localhost:8000/')
        .then(function (response) {
            console.log('response.data:', response.data);
            console.log('response.status =', response.status);
            
            const usersTable = document.getElementById('usersTable');
            const usersData = document.createElement('table');
            const tableTitle = document.createElement('th');
            const colunsTable = document.createElement('tr');
            const columName = document.createElement('th');
            const columEmail = document.createElement('th');

            usersData.setAttribute('border', '1');
            tableTitle.textContent = 'Users';
            tableTitle.setAttribute('colspan', '3');
            tableTitle.setAttribute('id', 'tableTitle');
            columName.textContent = 'name';
            columName.setAttribute('class', 'tableColumns');
            columName.setAttribute('id', 'columName');
            columEmail.textContent = 'e-mail';
            columEmail.setAttribute('class', 'tableColumns');
            columEmail.setAttribute('id', 'columEmail');

            colunsTable.appendChild(columName);
            colunsTable.appendChild(columEmail);
            usersData.appendChild(tableTitle);
            usersData.appendChild(colunsTable);
            usersTable.appendChild(usersData);

            response.data.forEach(user => {
                const userData = document.createElement('tr');
                const userName = document.createElement('th');
                const userEmail = document.createElement('th');

                userName.textContent = `${user.name}`;
                userName.setAttribute('class', 'columName');
                userEmail.textContent = `${user.email}`;
                userEmail.setAttribute('class', 'columEmail');

                userData.appendChild(userName);
                userData.appendChild(userEmail);
                usersData.appendChild(userData);
            });
        })
        .catch(function (error) {
            console.error('error-type:', error.response.data);
            console.error('error-status =', error.response.status);
        });


}
