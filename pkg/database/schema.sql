CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    is_doctor BOOLEAN NOT NULL
);

CREATE TABLE user_info (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users ON DELETE CASCADE NOT NULL,
    key TEXT NOT NULL,
    value TEXT
);

CREATE TABLE appointments (
    id SERIAL PRIMARY KEY,
    patient_id INTEGER REFERENCES users ON DELETE CASCADE NOT NULL,
    doctor_id INTEGER REFERENCES users ON DELETE SET NULL,
    time_at TIMESTAMP NOT NULL,
    appointment_type TEXT NOT NULL, 
    symptom TEXT DEFAULT ''
);

CREATE TABLE prescriptions (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    amount_per_day INTEGER NOT NULL
);

CREATE TABLE user_prescriptions (
    id SERIAL PRIMARY KEY,
    prescription_id INTEGER REFERENCES prescriptions ON DELETE CASCADE NOT NULL,
    user_id INTEGER REFERENCES users ON DELETE CASCADE NOT NULL,
    visible BOOLEAN DEFAULT TRUE
);

CREATE TABLE messages (
    id SERIAL PRIMARY KEY,
    user1_id INTEGER REFERENCES users ON DELETE SET NULL,
    user2_id INTEGER REFERENCES users ON DELETE SET NULL,
    content TEXT NOT NULL,
    sent_at TIMESTAMP NOT NULL
);