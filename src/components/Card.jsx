import styles from "../styles/Card.module.css";

export const Card = ({ task }) => {
  const statusColor = (status) => {
    switch (status) {
      case "PENDIENTE":
        return styles.status_pendiente;
      case "REALIZANDOSE":
        return styles.status_realizandose;
      case "REALIZADA":
        return styles.status_realizada;
      default:
        return styles.status_cancelada;
    }
  };

  return (
    <div className={styles.card}>
      <div className={styles.status}>
        <span className={`${styles.status_btn} ${statusColor(task.estado)}`}>{task.estado}</span>
      </div>
      <h3 className={styles.title}>{task.nombre}</h3>
      <p className={styles.description}>{task.descripcion}</p>
      <p className={styles.date}>{task.fechaVencimiento}</p>
    </div>
  );
};
