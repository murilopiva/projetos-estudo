import express, { response } from 'express';

const app = express();

app.get('/users', (request, response) =>{
    console.log('listagem de usarios');

    //response.send('hello world')

    response.json([
        'Diego',
        'Murilo',
        'Pomba',
        'teste'
    ])
});

app.post('/users', (request, response) => {
    const user = {
        name: 'Murilo',
        email: 'murilo@gmail.com'
    }

    //tem que por o return pq se tiver mais coisa abaixo, o código continua executnado
    return response.json  (user)
})

app.listen(3333)
