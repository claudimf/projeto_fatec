require 'rails_helper'

RSpec.describe "reads/show", type: :view do
  before(:each) do
    @read = assign(:read, Read.create!(
      temperature: "9.99"
    ))
  end

  it "renders attributes in <p>" do
    render
    expect(rendered).to match(/9.99/)
  end
end
