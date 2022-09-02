export async function loginApi(email, password) {
    const myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");

    const raw = JSON.stringify({
        email,
        password
    });

    const requestOptions = {
    method: 'POST',
    headers: myHeaders,
    body: raw,
    redirect: 'follow'
    };

    let response;
    try {
        response = await fetch("http://localhost:8000/api/token/", requestOptions);
    } catch (error) {
        console.log(error);
        return null;
    }
    if (response.status === 200) {
        const data = await response.json();
        return data;
    }
    return {
        error: true,
    }
}