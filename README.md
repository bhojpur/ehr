# Bhojpur EHR - Electronic Health Record

The `Bhojpur EHR` is an electronic health record management engine applied within
the [Bhojpur.NET Platform](https://github.com/bhojpur/platform/) for delivery of
distributed `applications` or `services`.

## Build Source Code

Firstly, you need `Python` >= 3.8. Install it, then issue the following commands.

```bash
sudo pip3 install -U -r requirements.txt
```

You can run the web application using the following commands.

```bash
cd pkg
gunicorn -b :8080 app:app
```

Then, open `http://localhost:8080` in a web-browser of your choice.
