import { ROUTE_LOCAL } from './Routes';

export async function Content(content){ // verificar usuario

    return fetch(ROUTE_LOCAL+'cargar', {
        method: 'POST',
        headers: {
            Accept: "application/json",
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            content:content,

        
        }),
    });
}


export async function Content2(content){ // verificar usuario

    return fetch(ROUTE_LOCAL+'cargar', {
        method: "POST",
        headers: {
            Accept: "application/json",
            "Content-Type": "application/json",
        },
        body: content
    });
}