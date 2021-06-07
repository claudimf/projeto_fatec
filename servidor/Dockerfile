FROM ruby:2.7.1
RUN apt-get update -qq && apt-get install -y nodejs postgresql-client
RUN apt install libpq-dev
RUN apt install build-essential
RUN mkdir /myapp
WORKDIR /myapp
COPY Gemfile /myapp/Gemfile
COPY Gemfile.lock /myapp/Gemfile.lock
COPY . /myapp
RUN bundle install
RUN bundle update
RUN rm -f tmp/pids/server.pid

# Start the main process.
CMD ["rails", "server", "-b", "0.0.0.0"]
