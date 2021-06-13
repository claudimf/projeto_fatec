Rails.application.routes.draw do
  resources :reads do
    get :destroy_all, on: :collection
  end

  get 'send_read' => 'reads#send_read'

  root 'reads#index'
  # For details on the DSL available within this file, see https://guides.rubyonrails.org/routing.html
end
