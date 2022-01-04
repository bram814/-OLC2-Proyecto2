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

export async function Reporte4(label1, label2, label3, content, extension, grado, filter, time,predict, isPredict, filterDep, dep){

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
            predict: predict,
            isPredict: isPredict,
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

export async function Reporte6(label1, label2, label3, content, extension, grado, filter, time){

    return fetch(ROUTE_LOCAL + 'reporte6', {
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


export async function Reporte7(label1, label2, label3, content, extension, grado, filter, time, predict, isPredict){

    return fetch(ROUTE_LOCAL + 'reporte7', {
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


export async function Reporte8(label1, label2, label3, content, extension, grado, filter, time, predict, isPredict){

    return fetch(ROUTE_LOCAL + 'reporte8', {
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



export async function Reporte9(label1, label2, label3, content, extension, grado, filter, time){

    return fetch(ROUTE_LOCAL + 'reporte9', {
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

export async function Reporte10(label1, label2, label3, content, extension, grado, filter, time, compareCountry){

    return fetch(ROUTE_LOCAL + 'reporte10', {
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
            compareCountry: compareCountry
        }),
    })

}

export async function Reporte11(label1, label2, label3, content, extension, filter){

    return fetch(ROUTE_LOCAL + 'reporte11', {
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
            filter: filter,
        }),
    })

}

export async function Reporte12(label1, label2, label3, content, extension, grado, filter, time, compareCountry){

    return fetch(ROUTE_LOCAL + 'reporte12', {
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
            compareCountry: compareCountry
        }),
    })

}