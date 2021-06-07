require 'rails_helper'

RSpec.describe "reads/index", type: :view do
  before(:each) do
    assign(:reads, [
      Read.create!(
        temperature: "9.99"
      ),
      Read.create!(
        temperature: "9.99"
      )
    ])
  end

  it "renders a list of reads" do
    render
    assert_select "tr>td", text: "9.99".to_s, count: 2
  end
end
