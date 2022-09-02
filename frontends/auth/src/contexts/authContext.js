import {
    createContext,
    useContext,
    useState,
  } from "react";
  
  import Cookies from "js-cookie";
import { loginApi } from "../api/login.api";
  
  const AuthContext = createContext({});
  AuthContext.displayName = "AuthContext";
  
  export const AuthProvider = ({ children }) => {
    const [token, setToken] = useState(Cookies.get("token"));
  
  
    const login = async (username, password) => {
      console.log(
        "Should hit the server with username and password",
        username,
        password
      );
  
      const data = await loginApi(username, password);
      console.log(data);
      const fakeToken = "fakeToken";
  
      Cookies.set("token", fakeToken);
      setToken(fakeToken);
    };
  
    const logout = () => {
      console.log("Will logout");
      Cookies.remove("token");
      setToken(undefined);
    };
  
    return (
      <AuthContext.Provider
        value={{
          token,
          login,
          logout,
        }}
      >
        {children}
      </AuthContext.Provider>
    );
  };
  
  export const useAuthContext = () => {
    const context = useContext(AuthContext);
    if (!context)
      throw new Error(`useAuthContext must be used within AuthProvider`);
  
    return context;
  };
  