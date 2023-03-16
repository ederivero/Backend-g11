import "./App.css";
import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import { SignIn } from "./pages/SignIn";
import { SignUp } from "./pages/SignUp";
import { Tasks } from "./pages/Tasks";
import { Profile } from "./pages/Profile";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<SignIn />} />
        <Route path="/registrarse" element={<SignUp />} />
        <Route path="/tareas" element={<Tasks />} />
        <Route path="/perfil" element={<Profile />} />
        <Route path="*" element={<Navigate to="/tareas" />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
