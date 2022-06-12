# Bhojpur EHR - Electronic Health Record

The `Bhojpur EHR` is an electronic health record management system applied within
the [Bhojpur.NET Platform](https://github.com/bhojpur/platform/) ecosystem for
delivery of distributed `applications` or `services`.

## Build Source Code

Firstly, you need `Python` >= 3.8. Install it, then issue the following commands.

```bash
sudo pip3 install -U -r requirements.txt
```

You can run the `Flask` web application using the following commands.

```bash
cd pkg
export SECRET_KEY=12345678
export WTF_CSRF_SECRET_KEY=12345678
export DATABASE_URL=postgres://bhojpur:welcome1234@127.0.0.1:5432
```

either, execute this

```bash
flask run --port=8080
```

or

```bash
gunicorn -b :8080 app:app
```

Then, open `http://localhost:8080` in a web-browser of your choice.
