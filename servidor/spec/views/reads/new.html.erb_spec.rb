require 'rails_helper'

RSpec.describe "reads/new", type: :view do
  before(:each) do
    assign(:read, Read.new(
      temperature: "9.99"
    ))
  end

  it "renders new read form" do
    render

    assert_select "form[action=?][method=?]", reads_path, "post" do

      assert_select "input[name=?]", "read[temperature]"
    end
  end
end
