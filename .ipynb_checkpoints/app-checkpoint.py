{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "84bb975f",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "\n",
      "\n",
      "====== WebDriver manager ======\n",
      "Current google-chrome version is 94.0.4606\n",
      "Get LATEST driver version for 94.0.4606\n",
      "Driver [/Users/marioacosta/.wdm/drivers/chromedriver/mac64/94.0.4606.61/chromedriver] found in cache\n"
     ]
    }
   ],
   "source": [
    "from flask import Flask, render_template, redirect, url_for\n",
    "from flask_pymongo import PyMongo\n",
    "import scraping\n",
    "app = Flask(__name__)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "8d714961",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Use flask_pymongo to set up mongo connection\n",
    "app.config[\"MONGO_URI\"] = \"mongodb://localhost:27017/mars_app\"\n",
    "mongo = PyMongo(app)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "64034b76",
   "metadata": {},
   "outputs": [],
   "source": [
    "@app.route(\"/\")\n",
    "def index():\n",
    "   mars = mongo.db.mars.find_one()\n",
    "   return render_template(\"index.html\", mars=mars)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "81f3bb24",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app '__main__' (lazy loading)\n",
      " * Environment: production\n",
      "\u001b[31m   WARNING: This is a development server. Do not use it in a production deployment.\u001b[0m\n",
      "\u001b[2m   Use a production WSGI server instead.\u001b[0m\n",
      " * Debug mode: off\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      " * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)\n",
      "[2021-10-02 23:59:47,234] ERROR in app: Exception on / [GET]\n",
      "Traceback (most recent call last):\n",
      "  File \"/Users/marioacosta/opt/anaconda3/envs/PythonData/lib/python3.9/site-packages/flask/app.py\", line 2070, in wsgi_app\n",
      "    response = self.full_dispatch_request()\n",
      "  File \"/Users/marioacosta/opt/anaconda3/envs/PythonData/lib/python3.9/site-packages/flask/app.py\", line 1515, in full_dispatch_request\n",
      "    rv = self.handle_user_exception(e)\n",
      "  File \"/Users/marioacosta/opt/anaconda3/envs/PythonData/lib/python3.9/site-packages/flask/app.py\", line 1513, in full_dispatch_request\n",
      "    rv = self.dispatch_request()\n",
      "  File \"/Users/marioacosta/opt/anaconda3/envs/PythonData/lib/python3.9/site-packages/flask/app.py\", line 1499, in dispatch_request\n",
      "    return self.ensure_sync(self.view_functions[rule.endpoint])(**req.view_args)\n",
      "  File \"<ipython-input-3-e191d5b2e6ba>\", line 4, in index\n",
      "    return render_template(\"index.html\", mars=mars)\n",
      "  File \"/Users/marioacosta/opt/anaconda3/envs/PythonData/lib/python3.9/site-packages/flask/templating.py\", line 148, in render_template\n",
      "    ctx.app.jinja_env.get_or_select_template(template_name_or_list),\n",
      "  File \"/Users/marioacosta/opt/anaconda3/envs/PythonData/lib/python3.9/site-packages/jinja2/environment.py\", line 1068, in get_or_select_template\n",
      "    return self.get_template(template_name_or_list, parent, globals)\n",
      "  File \"/Users/marioacosta/opt/anaconda3/envs/PythonData/lib/python3.9/site-packages/jinja2/environment.py\", line 997, in get_template\n",
      "    return self._load_template(name, globals)\n",
      "  File \"/Users/marioacosta/opt/anaconda3/envs/PythonData/lib/python3.9/site-packages/jinja2/environment.py\", line 958, in _load_template\n",
      "    template = self.loader.load(self, name, self.make_globals(globals))\n",
      "  File \"/Users/marioacosta/opt/anaconda3/envs/PythonData/lib/python3.9/site-packages/jinja2/loaders.py\", line 125, in load\n",
      "    source, filename, uptodate = self.get_source(environment, name)\n",
      "  File \"/Users/marioacosta/opt/anaconda3/envs/PythonData/lib/python3.9/site-packages/flask/templating.py\", line 59, in get_source\n",
      "    return self._get_source_fast(environment, template)\n",
      "  File \"/Users/marioacosta/opt/anaconda3/envs/PythonData/lib/python3.9/site-packages/flask/templating.py\", line 95, in _get_source_fast\n",
      "    raise TemplateNotFound(template)\n",
      "jinja2.exceptions.TemplateNotFound: index.html\n",
      "127.0.0.1 - - [02/Oct/2021 23:59:47] \"GET / HTTP/1.1\" 500 -\n"
     ]
    }
   ],
   "source": [
    "@app.route(\"/scrape\")\n",
    "def scrape():\n",
    "   mars = mongo.db.mars\n",
    "   mars_data = scraping.scrape_all()\n",
    "#.update(query_parameter, data, options)\n",
    "   mars.update({}, mars_data, upsert=True)\n",
    "   return redirect('/', code=302)\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "#    app.debug = True\n",
    " app.run()\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "PythonData",
   "language": "python",
   "name": "pythondata"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
