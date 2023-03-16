import { useEffect, useState, useRef } from "react";
import { useNavigate } from "react-router-dom";
import styles from "../styles/Header.module.css";

export const Header = () => {
  const [showDropdown, setShowDropdown] = useState(false);
  const dropdownRef = useRef(null);
  const navigate = useNavigate();

  useEffect(() => {
    const handleClickOutside = (event) => {
      if (dropdownRef.current && !dropdownRef.current.contains(event.target)) {
        setShowDropdown(false);
      }
    };

    document.addEventListener("click", handleClickOutside);
    return () => document.removeEventListener("click", handleClickOutside);
  }, []);

  const handleShowDropdown = () => {
    setShowDropdown(!showDropdown);
  };

  const signOut = () => {
    localStorage.removeItem("token");
    navigate("/");
  };

  return (
    <header className={styles.header}>
      <div className={styles.wrapper}>
        <span className={styles.logo} onClick={() => navigate("/tareas")}>
          TAREAS
        </span>
        <div className={styles.user} ref={dropdownRef}>
          <div onClick={handleShowDropdown} className={styles.user_content}>
            <div className={styles.user_photo}>
              <img
                src="https://avatars.githubusercontent.com/u/1000000?v=4"
                alt="Eduardo De Rivero"
              />
            </div>
            <span className={styles.user_name}>Eduardo De Rivero</span>
            <svg
              fill="#fff"
              width="25px"
              height="25px"
              viewBox="0 0 1024 1024"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path d="M759.2 419.8L697.4 358 512 543.4 326.6 358l-61.8 61.8L512 667z" />
            </svg>
          </div>

          <ul
            className={`${styles.dropdown} ${
              showDropdown && styles.dropdown_active
            }`}
          >
            <li className={styles.dropdown_item}>
              <a onClick={() => navigate("/perfil")}>Perfil</a>
            </li>
            <li className={styles.dropdown_item}>
              <a onClick={signOut}>Cerrar sesión</a>
            </li>
          </ul>
        </div>
      </div>
    </header>
  );
};
