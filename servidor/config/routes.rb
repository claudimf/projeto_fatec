Rails.application.routes.draw do
  resources :reads do
    get :get_read, on: :collection
  end

  root 'reads#index'
  # For details on the DSL available within this file, see https://guides.rubyonrails.org/routing.html
end
