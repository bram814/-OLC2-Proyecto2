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

export async function Reporte1(label1, label2, label3, content, extension, grado, filter, time){

    return fetch(ROUTE_LOCAL + 'reporte1', {
        method: 'POST',
        headers: {
            Accept: "application/json",
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            label1: label1,
            label2: label2,
            label3: label3,
            content: content,
            extension: extension,
            degree: grado,
            filter: filter,
            isTime: time
        }),
    })

}

export async function Reporte2(label1, label2, label3, content, extension, grado, filter, time, predict, isPredict){

    return fetch(ROUTE_LOCAL + 'reporte2', {
        method: 'POST',
        headers: {
            Accept: "application/json",
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            label1: label1,
            label2: label2,
            label3: label3,
            content: content,
            extension: extension,
            degree: grado,
            filter: filter,
            isTime: time,
            predict: predict,
            isPredict: isPredict
        }),
    })

}

export async function Reporte3(label1, label2, label3, content, extension, grado, filter, time){

    return fetch(ROUTE_LOCAL + 'reporte3', {
        method: 'POST',
        headers: {
            Accept: "application/json",
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            label1: label1,
            label2: label2,
            label3: label3,
            content: content,
            extension: extension,
            degree: grado,
            filter: filter,
            isTime: time
        }),
    })

}

export async function Reporte4(label1, label2, label3, content, extension, grado, filter, time, filterDep, dep){

    return fetch(ROUTE_LOCAL + 'reporte4', {
        method: 'POST',
        headers: {
            Accept: "application/json",
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            label1: label1,
            label2: label2,
            label3: label3,
            content: content,
            extension: extension,
            degree: grado,
            filter: filter,
            isTime: time,
            filterDep: filterDep,
            dep: dep
        }),
    })

}

export async function Reporte5(label1, label2, label3, content, extension, grado, filter, time, predict, isPredict, filterDep, dep){

    return fetch(ROUTE_LOCAL + 'reporte5', {
        method: 'POST',
        headers: {
            Accept: "application/json",
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            label1: label1,
            label2: label2,
            label3: label3,
            content: content,
            extension: extension,
            degree: grado,
            filter: filter,
            isTime: time,
            predict: predict,
            isPredict: isPredict,
            filterDep: filterDep,
            dep: dep
        }),
    })

}