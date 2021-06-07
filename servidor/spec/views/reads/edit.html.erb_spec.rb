require 'rails_helper'

RSpec.describe "reads/edit", type: :view do
  before(:each) do
    @read = assign(:read, Read.create!(
      temperature: "9.99"
    ))
  end

  it "renders the edit read form" do
    render

    assert_select "form[action=?][method=?]", read_path(@read), "post" do

      assert_select "input[name=?]", "read[temperature]"
    end
  end
end
