"use client";

import { useState } from "react";
import Image from "next/image";
import styles from "./Landing.module.css";

const members = [
  {
    name: "IRFAN SYAHPUTRA",
    role: "Bertanggung jawab sebagai blaablablabla",
    npm: "2308107010030",
    photo: "/team/irfan.png",
  },
  {
    name: "KHAIRUN NISA",
    npm: "230810701001O",
    role: "Bertanggung jawab sebagai blaablablabla",
    photo: "/team/nicun.png",
  },
  {
    name: "ANISA RAMAHDANI",
    npm: "2308107010008",
    role: "Bertanggung jawab sebagai blaablablabla",
    photo: "/team/nisa.png",
  },
  {
    name: "BUNGA RASIKHAH HAYA",
    npm: "2308107010010",
    role: "Bertanggung jawab sebagai blaablablabla",
    photo: "/team/bunga.png",
  },
];

export default function LandingPage() {
  const [isHovered, setIsHovered] = useState(false);

  return (
    <main className={styles.main}>
      {/* Gradient blur effect */}
      <div className={styles.gradientWrapper}>
        <div className={styles.blueBlur} />
        <div className={styles.purpleBlur} />
        <div className={styles.magentaBlur} />
      </div>

      {/* Hero section */}
      <div className={styles.content}>
        {/* Kiri: teks */}
        <div className={styles.left}>
          <div className={styles.badge}>
            <span className={styles.badgeDot} />
            Face Denoising Autoencoder
          </div>

          <h1 className={`${styles.title} ${styles.bebasHeading}`}>
            Bersihkan noise wajah
            <br />
            untuk era Face AI yang lebih tajam
          </h1>

          <p className={styles.desc}>
            FaceClean membersihkan noise, artefak kompresi, dan grain pada citra
            wajah dengan Convolutional Autoencoder yang dilatih khusus dataset
            wajah. Ideal untuk face recognition, presensi, dan arsip digital.
          </p>

          <p className={styles.subDesc}>
            Klik Start, unggah foto wajah, dan lihat perbandingan sebelum dan
            sesudah secara instan.
          </p>

          <a
            href="/denoise"
            onMouseEnter={() => setIsHovered(true)}
            onMouseLeave={() => setIsHovered(false)}
            className={
              isHovered
                ? `${styles.startButton} ${styles.startButtonHovered}`
                : styles.startButton
            }
          >
            Start
          </a>
        </div>

        {/* Kanan: hero */}
        <div className={styles.right}>
          <div className={styles.floorShadow} />
          <div className={styles.heroWrapper}>
            <Image
              src="/hero1.png"
              alt="FaceClean Hero"
              fill
              style={{ objectFit: "contain" }}
            />
          </div>
        </div>
      </div>

      {/* OUR TEAM section */}
      <section className={styles.teamSection}>
        <header className={styles.teamHeader}>
          <h2 className={styles.teamHeadingTop}>OUR TEAM</h2>
          <h3 className={styles.teamHeadingBottom}>AMAZING</h3>
          <div className={styles.teamDivider} />
        </header>
        
        <div className={styles.teamList}>
  {members.map((m, index) => (
    <article
      key={m.name}
      className={
        index % 2 === 0
          ? `${styles.teamCard} ${styles.teamCardEven}` // genap: foto kanan
          : styles.teamCard                               // ganjil: foto kiri
      }
    >
      <div className={styles.teamPhotoWrapper}>
        <Image
          src={m.photo}
          alt={m.name}
          width={260}
          height={360}
          className={styles.teamPhoto}
        />
      </div>
      <div className={styles.teamInfo}>
        <h4 className={styles.teamName}>{m.name}</h4>
        <h4 className={styles.teamNpm}>NPM: {m.npm}</h4>
        <p className={styles.teamRole}>{m.role}</p>
      </div>
    </article>
  ))}
</div>
      </section>
    </main>
  );
}
