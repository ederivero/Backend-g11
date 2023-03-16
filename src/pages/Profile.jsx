import { Header } from "../components/Header";
import styles from "../styles/Profile.module.css";

export const Profile = () => {
  return (
    <div className={styles.profile}>
      <Header />
      <div className={styles.profile_content}>
        <div className={styles.wrapper}>
          <div className={styles.profile_card}>
            <div className={styles.profile_card_header}>
              <div className={styles.profile_card_img}>
                <img
                  src="https://avatars.githubusercontent.com/u/1000000?v=4"
                  alt="Eduardo De Rivero"
                />
              </div>
            </div>
            <div className={styles.profile_card_body}>
              <h2 className={styles.profile_name}>Eduardo Ramiro</h2>
              <p className={styles.profile_last_name}>De Rivero</p>
              <div className={styles.profile_buttons}>
                <button>Editar</button>
                <button>Eliminar</button>
                <button>Más</button>
              </div>
              <p className={styles.profile_description}>
                Lorem ipsum dolor sit amet consectetur adipisicing elit.
                Laudantium inventore deleniti voluptas, nobis odit laboriosam
                minima consectetur soluta cupiditate cumque?
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};
