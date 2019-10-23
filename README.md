[![N|Solid](assets/img/django_logo_60px.png)](https://docs.djangoproject.com/en/2.2/)
# Django core
This is a pre built django project aiming to make project setup faster. It includes an environment file based configuration, a ready built template and static file structure, a gulp workflow for frontend works, and an empty *core* app.
## Usage:


### requirements.txt
First you need to install the dependencies. Navigate to the project root directory, and run:
`pip install -r requirements.txt`. It gets all the python packages you need.


### .env
Create a `.env` file in the root directory based on the `.env.example` file. The project will load sensitive data and config from here.

### Gulp workflow
This gulp workflow is meant to make your template building process faster and easier. To set it up, navigate yourself into the *template_workflow* directory, where *gulpfile.js* is located, and go through the followings.
1. install node.js to be able to use npm package manager
2. run: `npm install -global gulp-cli`
3. install the necessary node modules: `npm install`
4. run the gulp tasks: `gulp`
5. To start building, run: `gulp watch`


You are ready to work!

Version: 1.1

For help, contact: nyitrai.done@gmail.com
