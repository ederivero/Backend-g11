import { Suspense, useEffect, useState } from "react";
import { Navigate } from "react-router-dom";
import { Card } from "../components/Card";
import { Header } from "../components/Header";
import styles from "../styles/Tasks.module.css";
import { Modal } from "../components/Modal";

export const Tasks = () => {
  const [tasks, setTasks] = useState([]);
  const [showModal, setShowModal] = useState(false);

  useEffect(() => {
    const getData = async () => {
      const response = await fetch("http://127.0.0.1:5000/tareas", {
        headers: {
          Authorization: `Bearer ${localStorage.getItem("token")}`,
        },
      });
      const data = await response.json();
      setTasks(data.content);
    };
    getData();
  }, []);

  if (!localStorage.getItem("token")) {
    return <Navigate to="/" />;
  }

  return (
    <div className={styles.tasks}>
      <Header />

      <div className={styles.tasks_content}>
        <div className={styles.wrapper}>
          <Suspense fallback={<div>Loading...</div>}>
            {tasks?.map((task) => (
              <Card task={task} key={task.id} />
            ))}
          </Suspense>
        </div>
      </div>

      <div className={styles.open_modal}>
        <div className={styles.wrapper}>
          <button
            className={styles.open_modal_btn}
            onClick={() => setShowModal(true)}
          >
            <svg
              width="30px"
              height="30px"
              viewBox="0 0 24 24"
              fill="none"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                fillRule="evenodd"
                clipRule="evenodd"
                d="M12 3a1 1 0 0 0-1 1v7H4a1 1 0 1 0 0 2h7v7a1 1 0 1 0 2 0v-7h7a1 1 0 1 0 0-2h-7V4a1 1 0 0 0-1-1z"
                fill="#ffffff"
              />
            </svg>
          </button>
        </div>
      </div>

      <Modal
        setTasks={setTasks}
        setShowModal={setShowModal}
        showModal={showModal}
      />
    </div>
  );
};
