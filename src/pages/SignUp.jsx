import { useState } from "react";
import styles from "../styles/Sign.module.css";

export const SignUp = () => {
  const [userData, setUserData] = useState({
    username: "",
    password: "",
    confirmPassword: "",
  });

  const handleInputChange = (e) => {
    setUserData({ ...userData, [e.currentTarget.name]: e.currentTarget.value });
  };

  const signUp = async (e) => {
    e.preventDefault();
    const response = await fetch("http://127.0.0.1:5000/registro", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(userData),
    });
    const status = response.status;
    const data = await response.json();
    if (status === 200) {
      navigate("/");
    } else {
      setAlert({ message: data.message, type: "error", show: true });
    }
  };

  return (
    <div className={styles.sign}>
      <div className={styles.image}></div>
      <div className={styles.content}>
        <form className={styles.form} onSubmit={signUp}>
          <h1 className={styles.title}>Registrarse</h1>
          <div className={styles.form_group}>
            <label htmlFor="username">Username</label>
            <input
              type="text"
              placeholder="Username"
              onChange={handleInputChange}
            />
          </div>
          <div className={styles.form_group}>
            <label htmlFor="password">Password</label>
            <input
              type="password"
              placeholder="Password"
              onChange={handleInputChange}
            />
          </div>
          <div className={styles.form_group}>
            <label htmlFor="password">Confirm Password</label>
            <input
              type="password"
              placeholder="Confirm Password"
              onChange={handleInputChange}
            />
          </div>
          <button className={styles.sign_in_btn} type="button">
            Registrarse
          </button>
          <button className={styles.sign_up_btn} type="submit">
            Iniciar Sesión
          </button>
        </form>
      </div>
    </div>
  );
};
