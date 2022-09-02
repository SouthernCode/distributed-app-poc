import { useState } from 'react';
import { useAuthContext } from "../contexts/authContext";

export default function LoginForm() {
    const { login } = useAuthContext();
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    
    const handleSubmit = (e) => {
        e.preventDefault();
        login(username, password);
    }
    return (
        <form onSubmit={handleSubmit}>
        <label htmlFor="username">Username</label>
        <input type="text" id="username" value={username} onChange={(e) => setUsername(e.target.value)} />
        <label htmlFor="password">Password</label>
        <input type="password" id="password" value={password} onChange={(e) => setPassword(e.target.value)} />
        <button type="submit">Login</button>
        </form>
    )
}