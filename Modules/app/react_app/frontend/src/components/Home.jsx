import React from 'react'
import styles from '../styles.module.css'
import { Link } from 'react-router-dom'

const Home = () => {
    return (
        <div className={styles.topContainer}>
            <div className={styles.login}>
                <Link className={styles.logbtn} to='/login'>
                    Login
                </Link>
            </div>
            <div className={styles.info}>
                <h2>Audieyes</h2>
                <div className={styles.description}>
                    <h3>
                        Welcome to Audieyes, a groundbreaking project designed to empower the visually impaired community through innovative technology. Audieyes represents a leap forward in
                        accessibility, offering a suite of features that promise to enhance autonomy, safety, and quality of life for its users. Inspired by a commitment to inclusivity and the
                        transformative potential of technology, Audieyes aims to bridge the gap between the world's visual challenges and the possibilities afforded by digital innovation. ....
                    </h3>
                </div>
                <div className={styles.getStarted}>
                    <Link className={styles.btn} to='/upload'>
                        Get Started!
                    </Link>
                </div>
            </div>
        </div>
    )
}

export default Home
