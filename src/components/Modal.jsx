import styles from "../styles/Modal.module.css";
import { useState } from "react";

export const Modal = ({ setShowModal, showModal }) => {
  const [newTask, setNewTask] = useState({
    nombre: "",
    descripcion: "",
    fechaVencimiento: "",
    estado: "",
  });

  const handleInputChange = (e) => {
    setNewTask({
      ...newTask,
      [e.currentTarget.name]: e.currentTarget.value,
    });
  };

  const createTask = async (e) => {
    e.preventDefault();
    try {
      const response = await fetch("http://127.0.0.1:5000/tareas", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${localStorage.getItem("token")}`,
        },
        body: JSON.stringify({...newTask, fechaVencimiento: `${newTask.fechaVencimiento} 00:00:00`}),
      });
      const status = response.status;
      const data = await response.json();
      if (status === 201) {
        console.log(data);
      } else {
        console.log(data);
      }
    } catch (error) {
      console.log(error);
    }
  };

  return (
    <div className={`${styles.modal} ${showModal && styles.modal_active}`}>
      <div className={styles.modal_content}>
        <div className={styles.modal_header}>
          <span className={styles.modal_title}>Nueva Tarea</span>
          <button
            className={styles.modal_close}
            onClick={() => setShowModal(false)}
          >
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="20"
              height="20"
              viewBox="0 0 24 24"
              fill="none"
              stroke="currentColor"
              strokeWidth="2"
              strokeLinecap="round"
              strokeLinejoin="round"
            >
              <line x1="18" y1="6" x2="6" y2="18"></line>
              <line x1="6" y1="6" x2="18" y2="18"></line>
            </svg>
          </button>
        </div>
        <div className={styles.modal_body}>
          <form className={styles.form} onSubmit={createTask}>
            <div className={styles.form_group}>
              <label htmlFor="nombre">Ingresa el título</label>
              <input
                type="text"
                name="nombre"
                id="nombre"
                value={newTask.nombre}
                onChange={handleInputChange}
              />
            </div>
            <div className={styles.form_group}>
              <label htmlFor="descripcion">Ingresa la descripción</label>
              <input
                type="text"
                name="descripcion"
                id="descripcion"
                value={newTask.descripcion}
                onChange={handleInputChange}
              />
            </div>
            <div className={styles.form_group}>
              <label htmlFor="fechaVencimiento">
                Indica la fecha de vencimiento
              </label>
              <input
                type="date"
                name="fechaVencimiento"
                id="fechaVencimiento"
                value={newTask.fechaVencimiento}
                onChange={handleInputChange}
              />
            </div>
            <div className={styles.form_group}>
              <label htmlFor="estado">Selecciona el estado</label>
              <select
                name="estado"
                id="estado"
                value={newTask.estado}
                onChange={handleInputChange}
              >
                <option value="PENDIENTE">Pendiente</option>
                <option value="REALIZANDOSE">En progreso</option>
                <option value="REALIZADA">Completada</option>
                <option value="CANCELADA">Cancelada</option>
              </select>
            </div>

            <button className={styles.sign_in_btn}>Crear tarea</button>
          </form>
        </div>
      </div>
    </div>
  );
};
